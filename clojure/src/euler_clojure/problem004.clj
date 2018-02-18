(ns euler-clojure.problem004 
  (:require [clojure.string :as s]))

(defn divisors-in?
  "Returns true if x has two n-digit divisors."
  [l u x]
  (some #(and (zero? (mod x %)) (<= l (quot x %) u))
        (range u (dec l) -1)))

(defn >-palindrome-multiple
  "Return the greatest palindromic number multiple of two n-digits numbers."
  [n]
  (let [l (int (Math/pow 10 (dec n)))
        u (dec (* l 10))
        mirror-fn #(Integer/parseInt
                        (str % (s/reverse (str %))))
        divisors-fn (partial divisors-in? l u)]
    (first (filter divisors-fn (map mirror-fn (range u (dec l) -1))))))
