{-# LANGUAGE LambdaCase #-}
import Data.Char (toLower)
data StreamTrans i o a
    = Return a
    | ReadS (Maybe i -> StreamTrans i o a)
    | WriteS o (StreamTrans i o a)


listTrans :: StreamTrans i o a -> [i] -> ([o], a)
listTrans (Return x) _ = ([], x)
listTrans (ReadS f) [] = listTrans (f Nothing) []
listTrans (ReadS f) (i:is) = 
    let (out, res) = listTrans (f (Just i)) is
    in (out, res)
listTrans (WriteS o next) input = 
    let (out, res) = listTrans next input
    in (o : out, res)


toLowerTrans :: StreamTrans Char Char ()
toLowerTrans = ReadS ( \ case    
        Nothing -> Return ()
        Just c -> WriteS (toLower c) toLowerTrans )

main :: IO ()
main = do    
    print (take 3 $ fst $ listTrans toLowerTrans ['A','B','C','D'])
