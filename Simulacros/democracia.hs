votosEnBlanco :: [(String, String)] -> [Integer] -> Integer -> Integer
votosEnBlanco _ votos totalvotos | sumaVotos votos == totalvotos = 0
                                 | otherwise = totalvotos - sumaVotos (votos)

sumaVotos :: [Integer] -> Integer
sumaVotos [] = 0
sumaVotos (x:xs) = x + sumaVotos xs

formulasValidas :: [(String, String)] -> Bool
formulasValidas [] = True
formulasValidas ((x, y):xs) | x == y = False
                            | pertenece x xs || pertenece y xs = False
                            | otherwise = formulasValidas xs


pertenece :: String -> [(String, String)] -> Bool
pertenece _ [] = False
pertenece persona ((x, y):xs) | persona == x || persona == y = True
                              | otherwise = pertenece persona xs

cardinal :: [Integer] -> Integer
cardinal [] = 0
cardinal (x:xs) = 1 + cardinal xs

posicion :: String -> [(String, String)] -> Integer
posicion _ [] = 0
posicion elem ((x, y):xs) | elem == x = 1
                          | otherwise = 1 + posicion elem xs

posicionNum :: Integer -> [Integer] -> Integer
posicionNum n (x:xs) | n == x = 1
                    | otherwise = 1 + posicionNum n xs

posANum :: Integer -> [Integer] -> Integer
posANum 1 (x:xs) = x * 100
posANum n (x:xs) = posANum (n - 1) xs

porcentajeDeVotos :: String -> [(String, String)] -> [Integer] -> Float
porcentajeDeVotos presi formulas votos = division (posANum (posicion presi formulas) votos) (sumaVotos votos)


division :: Integer -> Integer -> Float 
division a b = (fromInteger a) / (fromInteger b)

proximoPresidente :: [(String, String)] -> [Integer] -> String
proximoPresidente formulas votos = cardinalFormulas (posicionNum (maximo votos) votos) formulas

cardinalFormulas :: Integer -> [(String, String)] -> String
cardinalFormulas 1 ((x, y):xs) = x
cardinalFormulas num ((x, y):xs) = cardinalFormulas (num - 1) xs


maximo :: [Integer] -> Integer 
maximo [x] = x 
maximo (x:y:xs) | x > y = maximo (x:xs)
                | otherwise = maximo (y:xs)




-- [("Juan", "Maria"), ("Manuel", "Gustavo"), ("Martin", "Matias")]