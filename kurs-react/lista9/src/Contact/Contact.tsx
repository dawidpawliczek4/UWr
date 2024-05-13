import React from "react";

interface ContactProps {}

const Contact: React.FC<ContactProps> = ({}) => {
  return (
    <div className="w-full h-screen flex flex-col justify-center items-center pb-[72px]">
      <p>Get In Touch</p>
      <div className="flex gap-x-4">
        <div>Here will be post image</div>
        <form className="flex flex-col">
          <label htmlFor="name">Name</label>
          <input type="text" name="name" id="name" className="rounded-md border-2 border-black bg-slate-800 outline-none" />
          <label htmlFor="email">Email</label>
          <input type="email" name="email" id="email" className="" />
          <label htmlFor="message">Message</label>
          <textarea name="message" id="message" cols={30} rows={10} className="rounded-md border-2 border-black bg-slate-800 outline-none"></textarea>
          <button type="submit">Send</button>
        </form>
      </div>
    </div>
  );
};

export default Contact;
