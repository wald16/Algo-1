estanRelacionados :: Integer -> Integer -> Bool
estanRelacionados  x y | x == 0 || y == 0 = error "No pueden ser 0"
                       | mod x y == 0 = True
                       | otherwise = False