(ns euler-clojure.problem002)

(defn fibo
  "Returns a lazy sequence of fibonacci numbers."
  ([] (fibo 1 2))
  ([a b] (lazy-seq (cons a (fibo b (+ b a))))))

(defn sum-even-fibonacci
  "Sum all even fibonacci numbers less than n."
  [n]
  (reduce + (filter even? (take-while #(< % n) (fibo)))))
