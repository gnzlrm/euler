(ns euler-clojure.problem005-test
  (:require [clojure.test :refer :all]
            [euler-clojure.problem005 :refer :all]))

(deftest t-lcm
  []
  (is (= 2520 (lcm 10)))
  (is (= 232792560 (lcm 20))))
