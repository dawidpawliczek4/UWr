import System.IO (isEOF)
import Data.Char (toLower)

echoLower :: IO ()
echoLower = do
    eof <- isEOF
    if eof
        then return ()
        else do
            c <- getChar
            putChar (toLower c)
            echoLower
    


main :: IO ()
main = do
    echoLower