import Data.List
row :: Integral a => [a] ->[a]
row ar = [fst p + (temp!!(snd p + 1))  | p <- pairs, snd p < ( length temp -1)]  
    where 
    pairs = zip temp [0..]  
    temp = (0:ar)++[0]
        

pas :: (Integral a, Integral b) =>  b -> [[a]] -> [[a]]
pas 1 ac = ac 
pas n ac = pas (n-1) (ac ++ [(row (last ac))])

pascal n = pas n [[1]]
prLn :: (Show a) => [a] -> String 
prLn nn = intercalate " " $ map show nn 

prLs [] = putStr "" 
prLs (x:xs) = do {putStrLn x; prLs xs; }

main = do 
      
    --putStrLn $ show $ [fst p | p <-pairs, snd p < (length temp -1)]
    --putStrLn $ show $ [fst p+ (temp!!(snd p +1)) | p <-pairs, snd p < (length temp -1)]
    --    where
    --    pairs = zip temp [0..]
    --    temp = [0,1,2,1,0] 
    --print $ row [1,2,1]
    n <- readLn :: IO Int
    --print $ pascal n 
    prLs [prLn x | x <- (pascal n)]
