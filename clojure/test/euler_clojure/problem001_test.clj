(ns euler-clojure.problem001-test
  (:require [euler-clojure.problem001 :as sut]
            [clojure.test :as t]))

(t/deftest mult-3-5-less-10-test
  (t/is (= 23 (sut/recur-sum-multiples-less-than 10 3 5)))
  (t/is (= 23 (sut/lazy-sum-multiples-less-than 10 3 5))))

(t/deftest mult-3-5-less-1000-test
  (t/is (= 233168 (sut/recur-sum-multiples-less-than 1000 3 5)))
  (t/is (= 233168 (sut/lazy-sum-multiples-less-than 1000 3 5))))

(t/deftest greater-mult-test
  (t/is (= 0 (sut/recur-sum-multiples-less-than 10 100)))
  (t/is (= 0 (sut/lazy-sum-multiples-less-than 10 100))))

