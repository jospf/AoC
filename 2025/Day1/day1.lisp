(defun update-combo (combo direction amount)
  "Move the COMBO dial left or right by AMOUNT in modulo-100 space."
  (mod (if (char= direction #\L)
           (- combo amount)
           (+ combo amount))
       100))

(defun count-zero-hits (filename &key (start 50))
  (with-open-file (in filename)
    (loop with combo = start
          with zeros = 0
          for line = (read-line in nil nil)
          while line
          do (let* ((direction (char line 0))
                    (amount (parse-integer (subseq line 1)))
                    (new-combo (update-combo combo direction amount)))
               (setf combo new-combo)
               (when (= combo 0)
                 (incf zeros)))
          finally (return zeros))))
