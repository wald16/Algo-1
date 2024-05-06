atajaronSuplentes :: [(String, String)] -> [Integer] -> Integer -> Integer
atajaronSuplentes _ goles golesTot = golesTot - sumaLista (goles)

sumaLista :: [Integer] -> Integer
sumaLista [] = 0
sumaLista (x:xs) = x + sumaLista xs


-----------------------------------------------------------------------------------------

equiposValidos :: [(String, String)] -> Bool
equiposValidos [] = True
equiposValidos ((x, y):xs) | x == y = False
                           | perteneceFst x xs = False
                           | perteneceSnd (x, y) xs = False
                           | otherwise = True
                    
perteneceFst :: String -> [(String, String)] -> Bool
perteneceFst _ [] = False
perteneceFst elem ((x, _):xs) = elem == x || perteneceFst elem xs


perteneceSnd :: (Eq a, Eq b) => (a, b) -> [(a, b)] -> Bool
perteneceSnd _ [] = False
perteneceSnd elem ((x, y):xs) = snd elem == y || perteneceSnd elem xs



equiposValidos' :: [(String, String)] -> Bool
equiposValidos' [] = True
equiposValidos' lista = noIguales lista && equiposValidos'' aplanado
    where 
          noIguales :: [(String, String)] -> Bool
          noIguales [] = True
          noIguales ((x, y):lista) = not (x == y) && noIguales lista

          aplanado = aplanar lista :: [String]
          equiposValidos'' :: [String] -> Bool
          equiposValidos'' [] = True
          equiposValidos'' (x:xs) = not (x `elem` xs) && equiposValidos'' xs
          
          

equiposValido' :: [(String, String)] -> Bool
equiposValido' [] = True
equiposValido' ((x, y):xs) | x == y = False 
                           | otherwise = checkIfValid x xs && checkIfValid y xs && equiposValido' xs

checkIfValid :: String -> [(String, String)] -> Bool
checkIfValid _ [] = True
checkIfValid elem ((x, y):xs) | elem == x || elem == y = False
                              | otherwise = checkIfValid elem xs


aplanar :: [(String, String)] -> [String]
aplanar [] = []
aplanar ((x, y):xs) = x : y : aplanar xs

---------------------------------------------------------------------------------------------------------

porcentajeDeGoles :: String -> [(String, String)] -> [Integer] -> Float
porcentajeDeGoles arquero lista goles = porcentajeDeGolesAux arquero lista goles

    where suma = sumaLista goles :: Integer
          porcentajeDeGolesAux :: String -> [(String, String)] -> [Integer] -> Float
          porcentajeDeGolesAux arquero ((_, y):xs) (l:ls) | arquero == y = (division (l) suma) * 100
                                                          | otherwise = porcentajeDeGolesAux arquero xs ls

division :: Integer -> Integer -> Float
division a b = fromInteger a / fromInteger b


-----------------------------------------------------------------------------------------------------------

vallaMenosVencida :: [(String, String)] -> [Integer] -> String
vallaMenosVencida [(_, arquero)] _ = arquero
vallaMenosVencida ((c1, arquero):(c2, arquero2):lista) (x:y:goles) | x < y = vallaMenosVencida ((c1, arquero):lista) (x:goles)
                                                                   | otherwise = vallaMenosVencida ((c2, arquero2):lista) (y:goles)
       
vallaMenosVencida' :: [(String, String)] -> [Integer] -> String
vallaMenosVencida' ((x, y):xs) (l:ls) | l == minimo (l:ls) = y
                                      | otherwise = vallaMenosVencida' xs ls 

minimo :: [Integer] -> Integer
minimo [x] = x
minimo (x:y:xs) | x < y = minimo (x:xs)
                | otherwise = minimo (y:xs)
-- [("boca", "manu"), ("river", "matias"), ("river", "marto"), ("racin", "dope")] [20, 30, 40, 10] 7

