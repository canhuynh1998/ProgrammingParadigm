; CS152 Fall 2022 
; Hoc Can Huynh
; 014836757
; Homework assignment 5 
; Exercise 3

(define reverse
    (lambda (list_number)
        (if (null? list_number)
            list_number
            (if (null? (cdr list_number))
                list_number
                (cons (car (reverse (cdr list_number)))
                      (reverse
                          (cons (car list_number)
                                (reverse
                                    (cdr (reverse (cdr list_number))))))
                      )
                )
            )
        )
)
(display (reverse '(1 2 3 4 5 6 7 8 9 10)))
(newline)
