(defun count-zero-passes (filename &key (start 50))
  "Count how many times the dial passes or lands on 0 while applying moves in FILENAME."
  (with-open-file (in filename)
    (loop with combo = start
          with zeros = 0
          for line = (read-line in nil nil)
          while line
          do (let* ((direction (char line 0))
                    (amount (parse-integer (subseq line 1)))
                    (zero-hits
                      (if (char= direction #\L)
                          (let* ((first-hit (if (zerop combo) 100 combo)))
                            (if (>= amount first-hit)
                                (1+ (floor (- amount first-hit) 100))
                                0))
                          (let* ((first-hit (let ((steps (mod (- 100 combo) 100)))
                                              (if (zerop steps) 100 steps))))
                            (if (>= amount first-hit)
                                (1+ (floor (- amount first-hit) 100))
                                0)))))
               (incf zeros zero-hits)
               (setf combo (mod (if (char= direction #\L)
                                    (- combo amount)
                                    (+ combo amount))
                                100)))
          finally (return zeros))))

(defun main ()
  (let* ((base (or *load-truename* *default-pathname-defaults*))
         (input (merge-pathnames "input.txt" base)))
    (format t "~A~%" (count-zero-passes input))))
