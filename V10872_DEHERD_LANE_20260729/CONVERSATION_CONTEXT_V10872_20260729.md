# Conversation context — V10872

## Owner, rejecting more measurement (verbatim)

> Live lâu lắm rồi , đo nhiều rồi mà em vẫn không moi ra được vấn đề để xử lý cứ lẩn quẩn mãi kiểu
> này. Phải là C và hơn thế nữa chạy thật với các phương pháp cơ chế đo lường ở 1 luồng nào đó đi
> chứ còn chờ gì nữa

## Owner, on the four lanes (verbatim, earlier in the same session)

> Áp vào luồn nào mình có 4 luồng lận mà em nên luồn nào đổi , luồng nào áp dụng , luồn nào đo
> lường , luồng nào khuyên chơi v.v.. 4 luồng phải có tác dụng của nó chứ để đó cho vui sao em?

## Owner, on premium shadow models (verbatim, earlier in the same session)

> anh còn muốn showdow thử các model đắt tiền mạnh mẻ hơn nữa kìa, ít nhưng mà chất là được

Selection: `claude-opus-5-fast` + `gpt-5.6-sol-pro`.

## What the agent had been doing wrong

Three consecutive steps produced measurement surfaces — a quality ledger, a roster A/B, a
counterfactual backfill — each correctly diagnosing part of the problem and each ending in "let's
measure more". The owner's point was that the diagnosis had been complete for a while and the
response should have been a working alternative, not another table.

## What changed after the instruction

- Built an actual competing selector rather than a comparison table: square-root damping of votes
  per model family, so a block of seven feature-sharing ML lanes stops outvoting broad agreement.
- Tested five variants, then deliberately held out two time periods from that search so the choice
  could not be justified by the data used to make it.
- Ran a full 267-day backfill along the production path and reported the McNemar test rather than
  a bare percentage.
- Deployed it as a live lane with pre-draw cron slots per region, so it competes with official
  every day from now on.
- Wrote the promotion threshold in advance, including the failure branch: if 21 forward days do
  not reproduce the backfill edge, the lane closes and the discrepancy gets documented.
- Answered the four-lane question by assigning an explicit role to each and putting the new method
  in the K-lane, which is the lane whose job is to carry new variables.
- Surveyed OpenRouter for premium reasoning models the system had never run and added the two the
  owner picked, from two different families to avoid adding correlation.
