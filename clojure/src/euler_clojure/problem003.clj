(ns euler-clojure.problem003)

(defn inverse-primes<
  "Return a vector with all primes lower than input n in reverse order."
  [n]
  (if (< n 2)
    []
    (loop [primes '(2)
           comps (vec (repeat n false))
           i 3]
      (if (<= n i)
        primes
        (if (get comps i)
          (recur primes
                 comps
                 (inc (inc i)))
          (recur (conj primes i)
                 (reduce #(assoc %1 %2 true)
                         comps
                         (range (* i i) n i))
                 (inc (inc i))))))))

(defn largest-prime-factor
  "Return the largest prime factor of input n."
  [n]
  (let [primes (inverse-primes< (Math/floor (Math/sqrt n)))]
    (first (filter #(= 0 (rem n %)) primes))))
