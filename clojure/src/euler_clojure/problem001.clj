(ns euler-clojure.problem001)

(defn recur-sum-multiples-less-than
  "Return the sum of all multiples of [mults] lower than n. Implemented using tail-recursion."
  [n & mults]
  (loop [iter 1
         multiples #{0}
         remaining-mults mults]
    (if (empty? remaining-mults)
      (reduce + multiples)
      (let [remaining (filter #(> n (* iter %)) remaining-mults)]
        (recur (inc iter)
               (into multiples (map #(* iter %) remaining))
               remaining)))))

(defn lazy-sum-multiples-less-than
  "Return the sum of all multiples of [mults] lower than n. Implemented using lazy-sequences."
  [n & mults]
  (reduce + (set (apply concat (map #(range % n %) mults)))))
