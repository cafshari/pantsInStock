# pantsInStock
Playwright + Python project to alert when a specific pair of pants become in stock, in my size. The intentions of this project are to: 
1. Demonstrate basic knowledge/implementation of Playwright and Python
2. Serve as a restock notification service for myself

The project runs on a cron job: daily at 12:00:00 UTC (and can also be triggered manually), as per [main.yml](/.github/workflows/main.yml). If it finds the item to be in stock in the specified size, it will email me with the link to purchase. In any outcome, the Playwright trace will be uploaded for each workflow run, as an artifact.
