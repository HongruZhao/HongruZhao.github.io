# Verification and reproducibility appendix

The audited proof source is frozen at `cb6514892b7846d71ae81152293934409a4b4fe4`. Documentation and archived terminal receipts are delivered after that source freeze; every current Lean source and pinned configuration must still match the frozen replay manifest.

## Fresh source replay

From a clean checkout of the frozen source, with the pinned dependency packages and their foundation cache available, the executed command was:

```sh
python3 scripts/verify.py --fresh --threads 9 --max-concurrent 9
```

The project build directory was absent before execution. The clean clone linked only the pinned dependency packages. The replay rebuilt all 1,744 project modules in dependency order, using at most nine simultaneous single-threaded Lean processes, kernel trust level zero, memory limit 16,384 MiB per compiler and `maxSynthPendingDepth=3`. It then ran the exhaustive module-origin transitive axiom audit. The source manifest was checked before and after the replay. Exact commands, exit statuses, timings and all compiler logs are in `evidence/checkpoints/cb65148`.

The replay reuses the pinned Lean/Mathlib foundation cache and is not a fresh rebuild of Mathlib. Lean is `4.35.0-rc3`; Mathlib is `4beb549110aa44b87d699166cece6e3642bddf34`. All nine Git package revisions and their tracked source cleanliness are checked against `lean/lake-manifest.json`. No dependency update is needed or authorized by these replay instructions.

For a machine without dependency checkouts, materialize each Git package at the exact `rev` in `lean/lake-manifest.json`, use the toolchain in `lean/lean-toolchain`, and obtain or rebuild the corresponding foundation artifacts. Preserve the manifest bytes. Run the verification command from the project root only after those pinned dependencies are available. The archived receipts are historical evidence of this run; a new replay writes new local receipts.

## Exhaustive independent audit

The independent reviewer compiles its own probes in a separate prefix. It does not reuse an author-built new packet object as a fresh new proof. The full candidate artifacts must be local, regular files rebuilt during the recorded replay, with all 392 paired project sidecars accounted for. Import reachability from `KLS` and exact source/object/log hashes are checked.

The baseline has 19,158 declarations and 16,554 theorem constants. Original accepted packet environments are independently probed for all 415 additional declarations, including 402 theorems and 13 definitions. After the declared complete import-path mapping, the final name set is exactly their disjoint union: 19,573 declarations and 16,956 theorem constants. Every name, defining module, declaration kind and transitive axiom set is reconciled, not just the totals. All 568 exact named theorem/definition gates are checked independently. Endpoint-shaped definitions cannot satisfy theorem gates.

Only `propext`, `Classical.choice` and `Quot.sound` are allowed. The failing axiom audit examines all declarations originating in project modules, including private and generated declarations, and their transitive dependencies. Supplemental source scans reject added `axiom`/`constant`, `sorry`, `admit`, `native_decide`, unsafe declarations and replacement implementations. The project mathematical sources contain no custom `run_cmd`, `elab`/`elab_rules`, `initialize`/`builtin_initialize`, or `macro`/`macro_rules` commands; ordinary inherited attributes remain present. The separate audit driver uses metaprogramming to inspect declarations.

All 1,610 preceding nonaggregate proof sources and three configurations are byte preserved. All 133 new bodies remain exact, with 80 files changing 109 import lines. There are no new declaration collisions or overlaps with the baseline. All 133 new mathematical logs are empty. All preceding logs are byte-identical, retaining 595 diagnostics in 202 modules. These diagnostics are not represented as a warning-free build.

## Semantic correspondence

The final nine closing theorem types, original full target definitions, two-way class equivalence, absolute continuity, almost-everywhere gradient, finite-energy integrability, extended-energy convention, faithful infimum/supremum, nonempty examples and closed Minkowski normalization were independently reviewed. The original Job 45 definition bodies are preserved. Job 14's predicate defined as `False` is excluded as evidence.

Targeted source reviews cover 41 stochastic modules, 46 Taylor/spectral modules, the selected weak quadratic interfaces and the complete final endpoint file. The evidence records exactly which sources were read. This consists of one full fresh project rebuild, independent probes and exhaustive axiom/name/origin/kind reconciliation, together with cumulative source semantic reviews. It is not a claim of a second full project rebuild or a new complete rereading of every source.

## Evidence locations

| Evidence | Location |
|---|---|
| Full replay and all module logs | `evidence/checkpoints/cb65148/replay-receipt.json`, `source-rebuild-receipt.json`, `source-rebuild/` |
| Primary exhaustive axiom log | `evidence/checkpoints/cb65148/replay-axiom-audit.log` |
| Independent full audit and probes | `evidence/checkpoints/cb65148/independent-full-replay-review/` |
| Root source and semantic guards | `evidence/checkpoints/cb65148/source-pin-semantic-guards.json` |
| Exact frozen source identity | `evidence/checkpoints/cb65148/checkpoint-source.json` |
| Integration plan, preflight and body preservation | `evidence/post1611-integration/` |
| Independent integration/freezer review | `evidence/final-integration-independent/` |
| Independently accepted endpoint packet | `evidence/regularity-cheeger-independent/full-kls-verification/` |
| Full-class quadratic closure packet | `evidence/regularity-cheeger-independent/weak-moment-quadratic-bound/` |
| Stochastic and weak-interface semantic crosswalks | `evidence/final-route-semantic-reviews/` |
| Exact final endpoint types and source-backed semantic crosswalk | `evidence/final-endpoint-semantic-review/` |
| Hash-preserved progress snapshots | `progress-history/sha256.json` |

The release supplies the pinned project and evidence, including previous checkpoints. Its package manifest identifies the source checkpoint, documentation revision and archive checksum. Cached foundation binaries are not represented as project proof source. The user's preference is 6.1 Sol Max with multiple agents; no unavailable runtime model/reasoning setting is claimed to have been independently verified.
