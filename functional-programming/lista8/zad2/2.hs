{-# LANGUAGE LambdaCase #-}
import Data.Char (toLower)
import GHC.IO.Handle (isEOF)

data StreamTrans i o a
    = Return a
    | ReadS (Maybe i -> StreamTrans i o a)
    | WriteS o (StreamTrans i o a)


toLowerTrans :: StreamTrans Char Char ()
toLowerTrans = ReadS ( \ case    
        Nothing -> Return ()
        Just c -> WriteS (toLower c) toLowerTrans 
        )


runIOStreamTrans :: StreamTrans Char Char a -> IO a
runIOStreamTrans (Return x) = return x
runIOStreamTrans (ReadS f) = do
    eof <- isEOF
    if eof
        then runIOStreamTrans (f Nothing)
    else do
        c <- getChar
        runIOStreamTrans (f (Just c))
runIOStreamTrans (WriteS o next) = do
    putChar o
    runIOStreamTrans next

main :: IO ()
main = runIOStreamTrans toLowerTrans


