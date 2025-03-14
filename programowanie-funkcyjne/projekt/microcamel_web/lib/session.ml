open Lwt.Syntax
open Cohttp

type session_extension = (string, string) Hashtbl.t * (unit -> unit)

exception SessionData of session_extension

let add_session_to_request (req : Cohttp.Request.t)
                           (session_data : (string, string) Hashtbl.t)
                           (delete_session : unit -> unit)
  : Cohttp.Request.t
  =
  let new_value = SessionData (session_data, delete_session) in

  (* Pobierz dotychczasowe extensions: *)
  let old_exts = Cohttp.Request.extensions req in
  (* To jest mapa typu string -> exn (zazwyczaj [String.Map.t exn]). *)

  (* Dodaj lub nadpisz wpis pod naszym session_key: *)
  let new_exts = String.Map.add session_key new_value old_exts in

  (* Zbuduj nowy obiekt Request, kopiując wszystkie pola
     (method, uri, version, headers, itp.) i podstawiając new_exts *)
  Cohttp.Request.make
    ~meth:(Cohttp.Request.meth req)
    ~uri:(Cohttp.Request.uri req)
    ~version:(Cohttp.Request.version req)
    ~encoding:(Cohttp.Request.encoding req)
    ~headers:(Cohttp.Request.headers req)
    ~chunked:(Cohttp.Request.chunked req)
    ~extensions:new_exts
    ()


(* 3. Funkcja, która wyciąga z requesta dane sesji (jeśli istnieją). *)
let get_session_from_request (req : Request.t)
  : ((string, string) Hashtbl.t * (unit -> unit)) option =
  match Request.extension req session_key with
  | Some (SessionData (session_data, delete_session)) ->
      Some (session_data, delete_session)
  | _ ->
      None

(* session_store.ml *)
module type SESSION_STORE = sig
  type t
  type session_id = string
  type session_data = (string, string) Hashtbl.t

  val create : float -> t Lwt.t
  val get : t -> session_id -> session_data option Lwt.t
  val set : t -> session_id -> string -> string -> unit Lwt.t
  val create_session : t -> session_data -> session_id Lwt.t
  val remove : t -> session_id -> unit Lwt.t
end

module In_memory_store : SESSION_STORE = struct
  type session_id = string
  type session_data = (string, string) Hashtbl.t
  type session_entry = { data : session_data; expires_at : float }
  type t = {
    sessions : (session_id, session_entry) Hashtbl.t;
    mutex : Lwt_mutex.t;
    lifetime : float;
  }

  let create lifetime =
    let store = { sessions = Hashtbl.create 100; mutex = Lwt_mutex.create (); lifetime } in
    (* Background cleanup every 5 minutes *)
    let rec cleanup () =
      let* () = Lwt_unix.sleep 300.0 in
      let now = Unix.gettimeofday () in
      let* () = Lwt_mutex.with_lock store.mutex (fun () ->
        Hashtbl.filter_map_inplace (fun _ entry ->
          if entry.expires_at > now then Some entry else None) store.sessions;
        Lwt.return ()
        ) 
      in
      cleanup ()
    in
    Lwt.async cleanup;
    Lwt.return store

  let get store id =
    Lwt_mutex.with_lock store.mutex (fun () ->
      let now = Unix.gettimeofday () in
      match Hashtbl.find_opt store.sessions id with
      | Some entry when entry.expires_at > now ->
          let new_entry = { entry with expires_at = now +. store.lifetime } in
          Hashtbl.replace store.sessions id new_entry;
          Lwt.return (Some entry.data)
      | Some _ | None ->
          Hashtbl.remove store.sessions id;
          Lwt.return None)

  let generate_session_id () =
    let random_char () =
      let chars = "abcdef0123456789" in
      let len = String.length chars in
      chars.[Random.int len]
    in
    let rec generate acc n =
      if n <= 0 then acc
      else generate (random_char () :: acc) (n - 1)
    in
    let id = String.of_seq (List.to_seq (generate [] 64)) in (* 64-character ID *)
    id

  let create_session store data =
    let id = generate_session_id () in (* Implement secure ID generation *)
    let now = Unix.gettimeofday () in
    let entry = { data; expires_at = now +. store.lifetime } in
    Lwt_mutex.with_lock store.mutex (fun () ->
      Hashtbl.add store.sessions id entry;
      Lwt.return id)

  let remove store id =
    Lwt_mutex.with_lock store.mutex (fun () ->
      Hashtbl.remove store.sessions id;
      Lwt.return ())      

  let set store id key value =
    Lwt_mutex.with_lock store.mutex (fun () ->
      match Hashtbl.find_opt store.sessions id with
      | Some entry ->
          Hashtbl.replace entry.data key value;
          Lwt.return ()
      | None ->
          Lwt.return () (* Session does not exist, do nothing *)
    )
end