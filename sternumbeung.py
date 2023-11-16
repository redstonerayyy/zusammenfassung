def sternUmbegung(b, rf) -> int:
    cs = b.getItem()

    count = 0

    if not (rf.p1 == cs.p1 and rf.p2 == cs.p2):
        if abs(rf.p1 - cs.p1) <= 5 and  abs(rf.p2 - cs.p2) <= 5:
            count += 1

    if b.hasLeft():
        count += sternUmbegung(b.getLeft(), rf)

    if b.hasRight():
        count += sternUmbegung(b.getRight(), rf)

    return count
