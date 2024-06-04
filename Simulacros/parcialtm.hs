hayQueCodificar :: Char -> [(Char, Char)] -> Bool
hayQueCodificar c [] = False
hayQueCodificar c ((x, y):xs) | c == x = True
                              | otherwise = hayQueCodificar c xs


-- 'a' "matias" [('a', 'b'), ('x', 'c'), ('d', 'e')] 

cuantasVecesHayQueCodificar :: Char -> [Char] -> [(Char, Char)] -> Integer
cuantasVecesHayQueCodificar c frase mapeo | hayQueCodificar c mapeo == False = 0
                                          | otherwise = contador c frase

contador :: Char -> [Char] -> Integer 
contador _ [] = 0
contador c (x:xs) | c == x = 1 + contador c xs
                  | otherwise = contador c xs


laQueMasHayQueCodificar :: [Char] -> [(Char, Char)] -> Char
laQueMasHayQueCodificar frase mapeo = cualApareceMas (checkFraseCodifica frase mapeo)

cualApareceMas :: [Char] -> Char
cualApareceMas [x] = x
cualApareceMas (x:y:xs) | contador x (x:y:xs) >= contador y (x:y:xs) = cualApareceMas (x:xs)
                        | otherwise = cualApareceMas (y:xs)

checkFraseCodifica :: [Char] -> [(Char, Char)] -> [Char]
checkFraseCodifica [] _ = []
checkFraseCodifica (x:xs) mapeo | hayQueCodificar x mapeo == True = x : checkFraseCodifica xs mapeo
                                | otherwise = checkFraseCodifica xs mapeo

codificarFrase :: [Char] -> [(Char, Char)] -> [Char]
codificarFrase (x:xs) mapeo = codificarFrase' (x:xs) mapeo              
       where codificarFrase' :: [Char] -> [(Char, Char)] -> [Char]
             codificarFrase' [] _ = []
             codificarFrase' (x:xs) ((l, y):ls) | hayQueCodificar x mapeo = y : codificarFrase' xs ls
                                                | otherwise = x : codificarFrase' xs mapeo




