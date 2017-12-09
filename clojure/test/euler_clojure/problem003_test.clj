(ns euler-clojure.problem003-test
  (:use [euler-clojure.problem003]
        [clojure.test]))

(deftest t-inverse-primes<
  []
  (is (= '(7 5 3 2) (inverse-primes< 10))))

(deftest t-largest-prime-factor
  []
  (is (= 29 (largest-prime-factor 13195)))
  (is (= 6857 (largest-prime-factor 600851475143))))
