(ns euler-clojure.problem004-test
  (:use [euler-clojure.problem004]
        [clojure.test]))

(deftest t->-palindrome-multiple?
  []
  (is (= (>-palindrome-multiple 2) 9009))
  (is (= (>-palindrome-multiple 3) 906609)))
