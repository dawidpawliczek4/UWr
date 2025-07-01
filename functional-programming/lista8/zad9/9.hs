module StreamTransMonad where
import Control.Monad

data StreamTrans i o a
    = Return a
    | ReadS (Maybe i -> StreamTrans i o a)
    | WriteS o (StreamTrans i o a)

instance Functor (StreamTrans i o) where
  fmap f m = m >>= (return . f)

instance Applicative (StreamTrans i o) where
  pure = Return
  (<*>) :: StreamTrans i o (a -> b) -> StreamTrans i o a -> StreamTrans i o b
  (<*>) = ap

instance Monad (StreamTrans i o) where
    (Return x) >>= f = f x
    (ReadS g) >>= f = ReadS $ \input -> g input >>= f
    (WriteS o next) >>= f = WriteS o (next >>= f)
