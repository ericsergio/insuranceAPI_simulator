# insuranceAPI_simulator
# built using gemini cli

✦ The mock Claims Adjuster Practice API and terminal glossary tool are fully implemented and verified.

  What Was Built:
   1. Database & Models (database.py, models.py):
      - SQLite backed by SQLAlchemy with tables for Claim, Task, and Term (glossary).
   2. Realistic Seeding & Dynamic Scenarios (seed.py):
      - Auto-seeds 15 foundational insurance concepts (FNOL, Subrogation, Deductibles, Actual Cash Value vs Replacement Cost, Bad Faith, etc.) with real adjuster practice contexts.
      - 5 diverse initial claims (rear-end bodily injury, frozen pipe water damage, multi-vehicle pileup with policy limits demand, total loss appraisal, parking collision).
      - Dynamic generator that produces randomized, realistic claims with prioritized diary tasks on demand.
   3. API Endpoints (main.py):
      - GET /api/claims (filterable by status, severity, claim_type)
      - GET /api/claims/{claim_id} (detailed claim file + task diary)
      - POST /api/claims (create claim)
      - POST /api/generate-scenario (generate randomized practice scenario)
      - GET /api/tasks/prioritized (adjuster diary queue sorted by urgency/severity & due date)
      - PATCH /api/tasks/{task_id} (update task status and notes)
      - GET /api/terms (searchable insurance terminology)
   4. Terminal CLI Tool (cli.py):
      - Interactive terminal browser or direct command-line flags to inspect definitions and practice claims.
   5. Test Suite (test_main.py):
      - 8 automated tests passing for all workflows.

  ---

  Quick Terminal Usage

  1. Interactive Adjuster CLI (Glossary & Claims)

   1 ./venv/bin/python3 cli.py
  Or single-command queries:

   1 ./venv/bin/python3 cli.py --term "subrogation"
   2 ./venv/bin/python3 cli.py --claims
   3 ./venv/bin/python3 cli.py --list

  2. Start the API Server
   1 ./run.sh
  Access interactive Swagger docs at: http://localhost:8000/docs

  3. Generate a Random Scenario via cURL

   1 curl -X POST http://localhost:8000/api/generate-scenario

  4. View Daily Prioritized Tasks via cURL

   1 curl http://localhost:8000/api/tasks/prioritized
