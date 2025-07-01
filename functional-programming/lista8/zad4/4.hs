{-# LANGUAGE LambdaCase #-}
import Data.Char (toLower)


data StreamTrans i o a
    = Return a
    | ReadS (Maybe i -> StreamTrans i o a)
    | WriteS o (StreamTrans i o a)


runCycle :: StreamTrans a a b -> b
runCycle trans = aux trans [] where
    aux (Return x) _ = x
    aux (ReadS f) [] = aux (f Nothing) []
    aux (ReadS f) (x:xs) = aux (f (Just x)) xs
    aux (WriteS o next) input = aux next (input ++ [o])

toLowerTrans :: StreamTrans Char Char ()
toLowerTrans = ReadS ( \ case    
        Nothing -> Return ()
        Just c -> WriteS (toLower c) toLowerTrans )

main :: IO ()
main = do
    print $ runCycle toLowerTrans    
