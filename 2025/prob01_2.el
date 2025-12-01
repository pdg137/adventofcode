(setq pos 50)
(setq count 0)

(defun turn (instruction)
  (let (
        (dir (substring instruction 0 1)) ; L or R
        (num (string-to-number (substring instruction 1)))
        )
    ;; if we're already on 0 and moving left, the following
    ;; will miscount by 1
    (if (and (eql pos 0) (equal dir "L"))
        (setq count (- count 1))
      )

    ;; do the turn
    (if (equal dir "L")
        (setq pos (- pos num))
      (setq pos (+ pos num))
      )

    ;; got back to 0 without going around
    (if (eql pos 0)
        (setq count (+ 1 count))
      )

    ;; going around past 99
    (while (> pos 99)
      (setq count (+ 1 count))
      (setq pos (- pos 100))
      )

    ;; going around past 0
    (while (< pos 0)
      (setq count (+ 1 count))
      (setq pos (+ pos 100))

      ;; final correction - ending on 0 from below
      (if (eql pos 0)
          (setq count (+ 1 count)))
      )
    )
  ;;(print (list instruction count pos))
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
