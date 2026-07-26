# Goobo Classifier Client

Next.js UI for **Goobo Classifier** (loan approval demo). Uses `public/logo.svg` in the header, `public/icon.svg` as the favicon, and the Goobo Labs brand system (mint `#3acc69`, Space Grotesk + Manrope).

## Run

1. Start the Flask API from `ds-ml-bootcamp/deployment/`:

```bash
python app.py
```

2. In another terminal:

```bash
cd client
npm install
npm run dev
```

Open [http://localhost:3000](http://localhost:3000).

Optional: set `NEXT_PUBLIC_API_URL=http://127.0.0.1:8000` in `.env.local` if needed.
