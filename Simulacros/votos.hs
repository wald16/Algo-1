porcentajeDeVotosAfirmativos :: [(String, String)] -> [Integer] -> Integer -> Float
porcentajeDeVotosAfirmativos _ votos votostotales = division (sumaVotos votos * 100) votostotales 

sumaVotos :: [Integer] -> Integer
sumaVotos [] = 0
sumaVotos (x:xs) = x + sumaVotos xs

division :: Integer -> Integer -> Float
division a b = (fromInteger a) / (fromInteger b)

---------------------------------------------------

formulasInvalidas :: [(String, String)] -> Bool
formulasInvalidas [] = False
formulasInvalidas ((x, y):xs) | x == y = True
                              | pertenece x xs || pertenece y xs = True
                              | otherwise = formulasInvalidas xs

pertenece :: String -> [(String, String)] -> Bool
pertenece _ [] = False
pertenece persona ((x, y):ys) | persona == x || persona == y = True
                              | otherwise = pertenece persona ys


porcentajeDeVotos :: String -> [(String, String)] -> [Integer] -> Float
porcentajeDeVotos vice formulas votos = division (checkVotosVice vice formulas votos ) (sumaVotos votos)


checkVotosVice :: String -> [(String, String)] -> [Integer] -> Integer
checkVotosVice vice ((x, y):xs) (l:ls) | vice == y = l * 100
                                       | otherwise = checkVotosVice vice xs ls


menosVotado :: [(String, String)] -> [Integer] -> String
menosVotado ((x, y):xs) (l:ls) | l == minimo (l:ls) = x
                               | otherwise = menosVotado xs ls 

minimo :: [Integer] -> Integer
minimo [x] = x
minimo (x:y:xs) | x < y = minimo (x:xs)
                | y < x = minimo (y:xs)


-- [("Juan", "Maria"), ("Manuel", "Gustavo"), ("Martin", "Matias")]

