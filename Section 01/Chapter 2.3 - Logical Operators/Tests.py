can_fly = True
is_blue = False
has_tail = False
can_see = True

print(has_tail or (is_blue and can_fly))

print(can_see and ((can_see or is_blue) and can_fly) or has_tail)

print((can_fly or has_tail) and (is_blue and has_tail))

