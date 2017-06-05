(ns euler-clojure.problem001)

(defn sum-multiples-less-than
  "Return the sum of all multiples of [mults] lower than n."
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
