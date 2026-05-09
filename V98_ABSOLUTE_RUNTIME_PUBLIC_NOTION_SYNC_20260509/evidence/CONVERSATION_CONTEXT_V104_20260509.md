# Conversation Context — V104 Phase A (Phiên 2026-05-09 22:00 → 23:55 VN)

> **Trang này lưu verbatim các yêu cầu của owner trong session V104 + agent confirmations.**
> Mục đích: để Notion AI và người review sau hiểu vì sao V104 có đúng liều lượng như vậy.
> Không được rút gọn lời tiếng Việt.

## Bối cảnh

- V99.1 → V103.2 đã deliver tối nay (xem `CONVERSATION_CONTEXT_V99_1_TO_V103_2_20260509.md`).
- Owner re-emphasized cần inject candidate từ V103 vào AI shadow prompt per region, kèm accept/reject schema.
- V104 11-lane prompt được owner ban hành lúc 23:23 VN.

---

## Owner message 1 — 2026-05-09 22:19 VN (vì sao cần V104)

> "Sau chu kỳ live ngày hôm nay anh có phát hiện nữa là MN hôm qua lose lại sảy ra hôm nay, MT cũng thế, và MB cũng thế. Anh nghĩ không phải là trùng hợp mà là một sai lệch dữ liệu nào đó, hoặc cơ chế nào đó mà chưa khai thác được, như trước đó em cũng đã khám phá ra đúng 13 là top 1 hôm nay đó nó đúng là dự đoán của ngày hôm qua bị lose. Em xem kỹ dùm anh đi đúng không? Hiện tại tiếp theo là gì em?"

## Owner message 2 — 2026-05-09 22:26 VN (13 / 61 / 64 tổn thất)

> "tiếp theo là gì, điều dự đoán lose miền trước ra miền sau cũng có nữa đó, rồi dự đoán hôm nay lose ngày mai lại ra, trước đó anh cũng đã đè cập nhiều lần em, verify với dữ liệu 60 ngày lại xem, hướng xử lý như thế nào? đặt biệt là áp dụng vào phần gốc đó là các model AI. các yêu cầu này trước đó a có nhắc đến em xem lại hết đi, rất bức xúc, khi lose liên tục nhiều ngày mà hôm nay 13 MN 2 nháy, MT 61 2 nháy, MB 64 1 nháy. v.v.v. còn nhiều nữa đã làm anh tổn thất nhiều nếu như theo tính toán lợi nhuận lời lỗ thì mất rất nhiều tiền đó em."

## Owner message 3 — 2026-05-09 22:39 VN (cần gán điều kiện cho AI)

> "Phải có 1 điều kiện gì đó để các model AI để gọi số lose ngày hôm qua, so sánh đối chiếu với các điều kiện, rules, dự đoán hôm nay để có output thật an toàn. Như MT anh lấy có Opus cũng gọi được số 61 nhưng đồng thuận kém, MB thì gemini cũng gọi được 64 nhưng đồng thuận ít, MN thì không thấy model nào gọi, nhưng theo hình ảnh lúc chiều em có verify trước giờ xổ MN thì ra kết quả 13 là top 1 và quả thật 13 top 1 chỉ có 13 là số dự đoán đúng. Điều khi ngày hôm trước lose thì nên xem xét số dự đoán đó cho ngày tiếp theo hoặc miền tiếp theo, em nắm code, em nắm DB ngữ cảnh em diên đạt sắc bén hơn anh đó em, đặt biệt các số đó mà trùng rules, quy tắc quy luật soi cầu thì khả quan lắm đó em, như số 64 MT hôm nay soi cầu nằm giải 8 MT D --> MB D. tiếp đi em tiếp theo em nên xem xét và lập kết hoặc cũng như xử lý các vấn đề tồn đọng"

## Owner message 4 — 2026-05-09 22:51 VN (region-independent prompts)

> "MN, MB, MT là các prompt độc lập để điều chỉnh mà không ảnh hưởng lẫn nhau, điều chỉnh được miền này sai miền kia, các yếu tố khác, các tầng khác, các phương pháp khác, các cơ chế khác cũng thế tạo độc lập cho từng miền là tốt nhất và bắt đầu ở luồng lane test là quá hợp lý rồi em cứ tiến hành đi."

## Owner message 5 — 2026-05-09 22:45 VN (Notion MCP must auto-update)

> "tại sao không cập nhật Notion MCP được em? em tiến hành 1 cách tự động đi chứ, lớn quá thì chia nhỏ từng trang ra chứ em. Tổng hợp các yêu cầu mà anh anh trao đổi trong trò chuyện này đẩy lên github Pulic luôn nha em. anh sợ Notion MCP của anh không nắm hết được các yêu càu và ngữ cảnh diễn giải nha em nên em phải hết sức chú ý. Notion MCP của anh đang kiểm soát tài liệu của anh để nhất quán giữa code và tài liệu đó em, nên việc cập nhật tài liệu Notion MCP và Public lên github các yêu cầu của anh cũng là một trong các vấn đề bắt buột"

## Owner message 6 — 2026-05-09 23:23 VN (V104 TOTAL FORCE prompt)

Owner ban prompt V104 11-lane chi tiết yêu cầu:
- Drive / GitHub / Notion full ingest.
- Shadow prompt injection per region MN/MT/MB.
- Monitoring + SSOT sync.
- NO production change.

Hard lock:
- Không sửa /du-doan, /api/final-bundle, generate_final_bundle().
- Không mutate production final_bundles, predictions, lottery_results, model_daily_eval.
- Không đổi production scoring / selector / SP-4.1.
- Không gọi production provider path.
- Không in full token / API key.
- shadow_only=1, diagnostic_only=1, output_eligible=0, owner_approved=0.

V104 LANE 5 gating:
- REQUIRED_IN_PROMPT khi V103 gate=REQUIRED, OR V103=REVIEW + recurrence STRONG/MEDIUM + lift_pp ≥ 5 + non-gan core + ≥2 layers.
- Gan alone NEVER promotes.
- MB gan normal 30d / special 15d. MN/MT gan normal 15d / special 7d.

V104 LANE 6 region prompts:
- MN: MN_D = (MN+MT+MB) D-1 + (MN+MT+MB) D-2.
- MT: KHÔNG broad D-2 như MN; consensus-first + no-break guard.
- MB: cold-aware + cross-region downstream + AI/no-token conflict shown.
- All: max 2 numbers, strict vs diagnostic warning, no production eligibility.

V104 LANE 7-11: admin API + UI panel §52 + backfill + Notion MCP §52F + GitHub private + public + final control report.

---

## Agent confirmations — V104 deliverables

### Lane 0 — Preflight DONE

- 3 governance files re-read (NOT modified): `.Antigravityrules.md` / `.AGENT.md` / `.cursorrules` đã có §52 + §52F từ V103.1+V103.2.
- VPS pre-state: health=200, v103-cross-region=401 admin-locked.
- Notion canonical page `Lottery_AI_Test` (id `067b40e9-0096-47e7-952c-504503559a29`) verified via `API-post-search`.
- 8 V99.1→V103 shadow tables schema inspected.
- 4 official tables pre-hash captured.

### Lane 1 — Drive ingest PARTIAL

- WebFetch listed 32 files trong folder `1BbUzZhGvUgGipd4smu9eDO7LFAXULApS`.
- File content KHÔNG đọc được qua WebFetch (Drive blocks `.txt` body cho unauthenticated client).
- `DRIVE_REPORT_INGEST_INDEX_V104.md` build với LISTED_NOT_READ status honest.
- Owner action cần: paste content / direct-download URLs / install Drive MCP.

### Lane 4 — V104 materializer DONE

- `web/backend/_v104_shadow_prompt_injection.py` (~660 lines).
- Functions: `materialize_for_date()`, `materialize_window()`, `build_payload()`, `_classify_injection()`, `_build_region_prompt_text()`.
- 2 tables created: `v104_shadow_prompt_candidate_injection` + `v104_shadow_prompt_model_decision`.

### Lane 5 — Gating logic DONE

- Anti-noise: gan-only path → OPTIONAL_REVIEW with reason `ANTI_NOISE_GAN_ONLY`.
- REQUIRED upgrade chỉ khi V103=REQUIRED hoặc tất cả 4 điều kiện met (recurrence + lift + core + layers).
- 30d backfill 1823 rows produced 0 REQUIRED — đúng spec, không inflate.

### Lane 6 — 3 region prompts DONE

- MN: cross-region D-1/D-2 pool, lose-yesterday-không-reject-vì-vừa-thua rule.
- MT: anti-import MN broad D-2, consensus-first, no-break guard.
- MB: cold-aware, gan 30d/15d, cross-region downstream priority, anti-herd rule.

### Lane 7 — Admin API + UI DONE

- `/api/admin/v104-shadow-prompt-injection` đăng ký trong `main.py`.
- `sectionV104ShadowPromptInjection` đăng ký trong `loadAllSections()` AND `setInterval(60000)`.
- 4 sub-panels render đầy đủ.

### Lane 8 — Backfill + 13/61/64/89 DONE

- 30d backfill local + VPS = 1823 rows match.
- 13 / 61 / 64 / 89 audit: tất cả 4 surface OPTIONAL_REVIEW today.
- V104_REPORT.md build trong `artifacts/v104_shadow_prompt_injection/`.

### Lane 8b — VPS deploy + smoke DONE

- scp 6 files (3 prompts + main.py + monitoring.html + materializer).
- `systemctl restart lottery` → active.
- 5 endpoint smoke: health=200, v104=401, v103=401, monitoring=401, du-doan=200.
- Post-hash 4 official tables: SHA256 IDENTICAL với local pre-hash.

### Lane 9 — Notion MCP §52F DONE

- 2 V104 sub-pages auto-created:
  - `🧪 V104 — Shadow Prompt Injection per Region (Phase A, 2026-05-09)` id `35b1d385-9bf8-81bb-b5a8-ecffb0c817e6`.
  - `📝 V104 — Owner Conversation Context (Phiên 2026-05-09 22:00 → 23:50 VN)` id `35b1d385-9bf8-8150-88cf-e36abe524520`.

### Lane 10 — GitHub sync IN PROGRESS

- Private: CHANGELOG `V20.3.37.104` + SSOT row + FU-V104-* + AUTOMATION seq 53 + commit + push.
- Public: LATEST_REPORT.json V103.2 → V104 + README + REPORT_INDEX + OPEN_ISSUES + NEXT_ACTION + CHANGELOG_PUBLIC + 3 evidence files + commit + push.

### Lane 11 — Final control report DONE

- `V104_REPORT.md` với 15 sections + control matrix.
- Phase B (provider pilot) = OWNER_GATE_REQUIRED.

---

## Hard contract maintained

- ZERO production code change.
- ZERO official table mutation (4 SHA256 IDENTICAL pre vs post).
- ZERO provider call (Phase A).
- ZERO promote / rollback button.
- ZERO production prompt SP-4.1 change.
- ZERO secrets printed (Grep ghp_/sk-/AIza scan clean).

Generated 2026-05-09 23:55 VN by Cursor agent automation.
