-- {-# LANGUAGE LambdaCase #-}
import Data.Char (toLower)

data StreamTrans i o a
    = Return a
    | ReadS (Maybe i -> StreamTrans i o a)
    | WriteS o (StreamTrans i o a)

(|>|) :: StreamTrans i m a -> StreamTrans m o b -> StreamTrans i o b
(|>|) _ (Return x) = Return x
(|>|) (ReadS f) trans2 = ReadS $ \input -> f input |>| trans2
(|>|) (WriteS m next1) (trans2) = connectStreams trans2 m next1

