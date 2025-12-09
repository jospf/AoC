(defun split-string (string delimiter)
  (let ((start 0)
        (parts '()))
    (loop for pos = (position delimiter string :start start)
          do (if pos
                 (progn
                   (push (subseq string start pos) parts)
                   (setf start (1+ pos)))
                 (progn
                   (push (subseq string start) parts)
                   (return))))
    (nreverse parts)))

(defun parse-range (token)
  (let ((dash (position #\- token)))
    (unless dash
      (error "Invalid range token: ~A" token))
    (let ((start (parse-integer token :end dash))
          (end (parse-integer token :start (1+ dash))))
      (cons start end))))

(defun lower-bound (vector value)
  (let ((low 0)
        (high (length vector)))
    (loop while (< low high) do
      (let ((mid (floor (+ low high) 2)))
        (if (< (aref vector mid) value)
            (setf low (1+ mid))
            (setf high mid))))
    low))

(defun upper-bound (vector value)
  (let ((low 0)
        (high (length vector)))
    (loop while (< low high) do
      (let ((mid (floor (+ low high) 2)))
        (if (<= (aref vector mid) value)
            (setf low (1+ mid))
            (setf high mid))))
    low))

(defun generate-repeated (max-end)
  (let* ((digits (length (write-to-string max-end)))
         (repeated (make-hash-table :test #'eql)))
    (loop for block-len from 1 to digits do
      (let* ((pow-block (expt 10 block-len))
             (block-start (/ pow-block 10))
             (block-limit (1- pow-block))
             (max-repeats (floor digits block-len)))
        (when (>= max-repeats 2)
          (loop for repeats from 2 to max-repeats do
            (let* ((pow-total (expt 10 (* block-len repeats)))
                   (multiplier (/ (1- pow-total) (1- pow-block)))
                   (limit-block (min block-limit (floor max-end multiplier))))
              (when (<= block-start limit-block)
                (loop for block from block-start to limit-block do
                  (setf (gethash (* block multiplier) repeated) t))))))))
    (sort (coerce (loop for k being the hash-keys of repeated collect k) 'vector) #'<)))

(defun prefix-sums (vector)
  (let* ((len (length vector))
         (pref (make-array (1+ len) :initial-element 0)))
    (loop for i from 0 below len do
      (setf (aref pref (1+ i)) (+ (aref pref i) (aref vector i))))
    pref))

(defun compute-total (ranges)
  (let* ((max-end (loop for (_ . end) in ranges maximize end))
         (repeated (generate-repeated max-end))
         (pref (prefix-sums repeated))
         (total 0))
    (loop for (start . end) in ranges do
      (let* ((l (lower-bound repeated start))
             (r (upper-bound repeated end)))
        (incf total (- (aref pref r) (aref pref l)))))
    total))

(defun main ()
  (let* ((line (with-open-file (in "input.txt")
                 (read-line in nil "")))
         (ranges (loop for token in (split-string line #\,)
                       unless (zerop (length token))
                       collect (parse-range token))))
    (format t "~A~%" (compute-total ranges))))

(main)
