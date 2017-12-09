(ns euler-clojure.problem002-test
  (:require  [clojure.test :as t])
  (:require  [euler-clojure.problem002 :as sut]))

(t/deftest less-10-sum
  (t/is (= 44 (sut/sum-even-fibonacci 100))))

(t/deftest less-4000000-sum
  (t/is (= 4613732 (sut/sum-even-fibonacci 4000000))))

(t/deftest fibo-10-terms
  (t/is (= [1 2 3 5 8 13 21 34 55 89] (take 10 (sut/fibo))))) 
