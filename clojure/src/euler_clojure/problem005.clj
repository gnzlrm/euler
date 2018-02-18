(ns euler-clojure.problem005
  (:require [euler-clojure.problem003 :refer :all]))


(defn great-pow-<
  "Return the greatest power of x lower than n."
  ([n x] (great-pow-< n x x))
  ([n x b] (if (>= (*' x b) n)
             x
             (recur n (*' x b) b))))


(defn lcm
  "Return the least common multiple of all numbers in range (2, n]."
  [n]
  (reduce *' (map (partial great-pow-< n) (inverse-primes< n))))
