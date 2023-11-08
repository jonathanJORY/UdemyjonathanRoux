import System.IO
main::IO()
main=do
  hSetBuffering stdout NoBuffering
  [lx,ly,tx,ty]<-map read.words<$>getLine
  let move(x,y)=(if y<ly then "S" else if y>ly then "N" else "")++(if x<lx then "E" else if x>lx then "W" else "")
  let loop(x,y)=do
      _<-getLine
      putStrLn$move(x,y)
      loop(x+signum(lx-x),y+signum(ly-y))
  loop(tx,ty)
