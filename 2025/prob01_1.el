(setq pos 50)
(setq count 0)

(defun turn (instruction)
  (let (
        (dir (substring instruction 0 1)) ; L or R
        (num (string-to-number (substring instruction 1)))
        )
    (if (equal dir "L")
        (setq pos (- pos num))
      (setq pos (+ pos num))
      )
    (setq pos (mod pos 100))
    (if (eql pos 0)
        (setq count (+ 1 count))
      )
    )
  )

(with-temp-buffer
  (insert-file-contents-literally "data01.txt")
  (while (not (eobp))
    (let ((beg (point)))
      (move-end-of-line nil)
      (turn (buffer-substring-no-properties beg (point)))
      (forward-char)
      )
    )
  )

(print count)
