"use client";

import { FormEvent, useEffect, useState } from "react";

type PredictResponse = {
  model: string;
  label: string;
  prediction: number;
  confidence?: number;
  error?: string;
};

type Theme = "light" | "dark";

const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://127.0.0.1:8000";
const THEME_KEY = "goobo-theme";

function applyTheme(theme: Theme) {
  document.documentElement.classList.toggle("dark", theme === "dark");
}

function modelLabel(model: string) {
  return model === "logistic_regression"
    ? "Logistic Regression"
    : "Random Forest";
}

export default function HomePage() {
  const [model, setModel] = useState<"lr" | "rf">("rf");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [result, setResult] = useState<PredictResponse | null>(null);
  const [theme, setTheme] = useState<Theme>("light");

  const [form, setForm] = useState({
    Income: "65000",
    CreditScore: "720",
    EmploymentYears: "5",
    LoanAmount: "15000",
    HasCollateral: "Yes",
    PreviousDefaults: "No",
  });

  useEffect(() => {
    const isDark = document.documentElement.classList.contains("dark");
    setTheme(isDark ? "dark" : "light");
  }, []);

  function toggleTheme() {
    const next: Theme = theme === "dark" ? "light" : "dark";
    setTheme(next);
    applyTheme(next);
    localStorage.setItem(THEME_KEY, next);
  }

  const update = (key: keyof typeof form, value: string) => {
    setForm((prev) => ({ ...prev, [key]: value }));
  };

  async function onSubmit(e: FormEvent) {
    e.preventDefault();
    setLoading(true);
    setError("");
    setResult(null);

    try {
      const body = {
        Income: Number(form.Income),
        CreditScore: Number(form.CreditScore),
        EmploymentYears: Number(form.EmploymentYears),
        LoanAmount: Number(form.LoanAmount),
        HasCollateral: form.HasCollateral,
        PreviousDefaults: form.PreviousDefaults,
      };

      const res = await fetch(`${API_URL}/predict?model=${model}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(body),
      });

      const data = await res.json();
      if (!res.ok) {
        throw new Error(data.error || `Request failed (${res.status})`);
      }
      setResult(data);
    } catch (err) {
      setError(
        err instanceof Error
          ? err.message
          : "Could not reach the API. Is Flask running on port 8000?"
      );
    } finally {
      setLoading(false);
    }
  }

  const approved = result?.label === "Approved";
  const confidence =
    typeof result?.confidence === "number" ? result.confidence : null;

  return (
    <main className="relative min-h-screen overflow-hidden">
      <div
        className="pointer-events-none absolute inset-0 opacity-70"
        style={{
          background:
            "radial-gradient(ellipse 80% 50% at 10% -10%, var(--glow), transparent 55%), radial-gradient(ellipse 60% 40% at 90% 0%, var(--glow-soft), transparent 50%)",
        }}
      />

      <div className="relative mx-auto flex min-h-screen max-w-5xl flex-col px-6 py-10 md:px-10">
        <header className="mb-12 flex items-center justify-between gap-4">
          <img
            src="/logo.svg"
            alt="Goobo Labs"
            className="h-9 w-auto md:h-10"
            width={240}
            height={68}
          />
          <button
            type="button"
            onClick={toggleTheme}
            className="cursor-pointer rounded-full border px-4 py-2 text-sm font-medium transition hover:opacity-90"
            style={{
              borderColor: "var(--border-strong)",
              background: "var(--surface)",
              color: "var(--ink)",
            }}
            aria-label={
              theme === "dark" ? "Switch to light mode" : "Switch to dark mode"
            }
          >
            {theme === "dark" ? "Light" : "Dark"}
          </button>
        </header>

        <div className="mb-8 max-w-xl">
          <h1 className="brand mb-3 text-4xl font-semibold leading-tight md:text-5xl">
            Check loan approval
          </h1>
          <p
            className="text-base leading-relaxed"
            style={{ color: "var(--muted)" }}
          >
            Enter an applicant profile. Goobo Classifier returns Approved or
            Rejected using the same Lesson 5 models you trained in class.
          </p>
        </div>

        <div className="grid flex-1 gap-10 lg:grid-cols-[1.1fr_0.9fr] lg:items-start">
          <section>
            <form
              onSubmit={onSubmit}
              className="rounded-2xl border p-6 md:p-8"
              style={{
                borderColor: "var(--border)",
                background: "var(--surface)",
                boxShadow: "0 20px 60px -40px var(--shadow)",
              }}
            >
              <div className="mb-6">
                <label
                  className="mb-2 block text-sm font-medium"
                  style={{ color: "var(--muted-strong)" }}
                >
                  Model
                </label>
                <div
                  className="inline-flex rounded-full p-1"
                  style={{ background: "var(--surface2)" }}
                >
                  {(
                    [
                      ["rf", "Random Forest"],
                      ["lr", "Logistic Regression"],
                    ] as const
                  ).map(([value, label]) => (
                    <button
                      key={value}
                      type="button"
                      onClick={() => setModel(value)}
                      className="cursor-pointer rounded-full px-4 py-2 text-sm font-medium transition"
                      style={
                        model === value
                          ? {
                              background: "var(--mint)",
                              color: "#0a0b0a",
                              boxShadow: "0 1px 2px rgba(12,12,11,0.12)",
                            }
                          : {
                              background: "transparent",
                              color: "var(--muted-strong)",
                            }
                      }
                    >
                      {label}
                    </button>
                  ))}
                </div>
              </div>

              <div className="grid gap-4 sm:grid-cols-2">
                <Field
                  label="Income"
                  value={form.Income}
                  onChange={(v) => update("Income", v)}
                  type="number"
                />
                <Field
                  label="Credit score"
                  value={form.CreditScore}
                  onChange={(v) => update("CreditScore", v)}
                  type="number"
                />
                <Field
                  label="Employment years"
                  value={form.EmploymentYears}
                  onChange={(v) => update("EmploymentYears", v)}
                  type="number"
                  step="0.1"
                />
                <Field
                  label="Loan amount"
                  value={form.LoanAmount}
                  onChange={(v) => update("LoanAmount", v)}
                  type="number"
                />
                <SelectField
                  label="Has collateral"
                  value={form.HasCollateral}
                  onChange={(v) => update("HasCollateral", v)}
                />
                <SelectField
                  label="Previous defaults"
                  value={form.PreviousDefaults}
                  onChange={(v) => update("PreviousDefaults", v)}
                />
              </div>

              <button
                type="submit"
                disabled={loading}
                className="mt-8 w-full cursor-pointer rounded-full px-6 py-3.5 text-base font-semibold transition hover:opacity-90 disabled:cursor-not-allowed disabled:opacity-60"
                style={{
                  background: "var(--mint)",
                  color: "#0a0b0a",
                }}
              >
                {loading ? "Checking…" : "Run Goobo Classifier"}
              </button>

              {error ? (
                <p className="mt-4 text-sm" style={{ color: "var(--error)" }}>
                  {error}
                </p>
              ) : null}
            </form>
          </section>

          <aside>
            <ResultPanel
              loading={loading}
              result={result}
              approved={approved}
              confidence={confidence}
            />
          </aside>
        </div>

        <footer
          className="mt-14 border-t pt-6"
          style={{ borderColor: "var(--border)" }}
        >
          <p className="brand text-base font-semibold tracking-tight">
            Goobo Classifier
          </p>
          <p className="mt-1 text-sm" style={{ color: "var(--muted)" }}>
            Loan approval · DS/ML Bootcamp
          </p>
          <p className="mt-3 max-w-2xl text-sm leading-relaxed" style={{ color: "var(--muted)" }}>
            AI can make mistakes sometimes. Always check the result and take the
            final decision yourself — this demo is for learning, not a real loan
            decision.
          </p>
          <p className="mt-3 flex flex-wrap gap-x-4 gap-y-1 text-sm">
            <a
              href="https://www.goobolabs.so/"
              target="_blank"
              rel="noopener noreferrer"
              className="underline-offset-4 transition hover:underline"
              style={{ color: "var(--mint-700)" }}
            >
              goobolabs.so
            </a>
            <a
              href="https://github.com/goobolabs/ds-ml-bootcamp"
              target="_blank"
              rel="noopener noreferrer"
              className="underline-offset-4 transition hover:underline"
              style={{ color: "var(--mint-700)" }}
            >
              GitHub · ds-ml-bootcamp
            </a>
          </p>
        </footer>
      </div>
    </main>
  );
}

function ResultPanel({
  loading,
  result,
  approved,
  confidence,
}: {
  loading: boolean;
  result: PredictResponse | null;
  approved: boolean;
  confidence: number | null;
}) {
  const panelStyle = result
    ? approved
      ? {
          borderColor: "rgba(58, 204, 105, 0.35)",
          background:
            "linear-gradient(165deg, color-mix(in srgb, var(--mint) 14%, var(--surface)) 0%, var(--surface) 55%)",
          boxShadow: "0 24px 50px -36px rgba(58, 204, 105, 0.55)",
        }
      : {
          borderColor: "var(--border-strong)",
          background:
            "linear-gradient(165deg, color-mix(in srgb, var(--ink) 6%, var(--surface)) 0%, var(--surface) 60%)",
          boxShadow: "0 20px 50px -40px var(--shadow)",
        }
    : {
        borderColor: "var(--border)",
        background: "var(--surface2)",
      };

  return (
    <div
      className="relative overflow-hidden rounded-2xl border p-6 md:min-h-[22rem] md:p-8"
      style={panelStyle}
      aria-live="polite"
    >
      {result && approved ? (
        <div
          className="pointer-events-none absolute -right-10 -top-10 h-40 w-40 rounded-full opacity-40"
          style={{
            background:
              "radial-gradient(circle, var(--mint) 0%, transparent 70%)",
          }}
        />
      ) : null}

      <div className="relative flex h-full flex-col">
        <div className="mb-6 flex items-center justify-between gap-3">
          <p
            className="text-sm font-medium uppercase tracking-[0.14em]"
            style={{ color: "var(--muted-label)" }}
          >
            Decision
          </p>
          {result ? (
            <span
              className="rounded-full px-3 py-1 text-xs font-semibold"
              style={{
                background: approved
                  ? "color-mix(in srgb, var(--mint) 22%, transparent)"
                  : "var(--surface2)",
                color: approved ? "var(--mint-700)" : "var(--muted-strong)",
              }}
            >
              {approved ? "Pass" : "Hold"}
            </span>
          ) : null}
        </div>

        {loading ? (
          <div className="flex flex-1 flex-col justify-center gap-4">
            <p
              className="brand pulse-soft text-3xl font-semibold"
              style={{ color: "var(--muted)" }}
            >
              Scoring applicant…
            </p>
            <div
              className="h-2 overflow-hidden rounded-full"
              style={{ background: "var(--border)" }}
            >
              <div
                className="h-full w-2/5 rounded-full"
                style={{
                  background: "var(--mint)",
                  animation: "meter-fill 1.1s ease-in-out infinite alternate",
                }}
              />
            </div>
          </div>
        ) : !result ? (
          <div className="flex flex-1 flex-col justify-center gap-3">
            <div
              className="mb-2 flex h-12 w-12 items-center justify-center rounded-2xl"
              style={{
                background: "var(--surface)",
                border: "1px solid var(--border)",
              }}
            >
              <img src="/icon.svg" alt="" className="h-6 w-6 opacity-70" />
            </div>
            <p
              className="brand text-3xl font-semibold leading-tight"
              style={{ color: "var(--muted-faint)" }}
            >
              Ready when you are
            </p>
            <p className="max-w-xs text-sm leading-relaxed" style={{ color: "var(--muted)" }}>
              Run a profile to see Approve / Reject with model confidence.
            </p>
          </div>
        ) : (
          <div key={`${result.label}-${result.model}-${confidence}`} className="result-enter flex flex-1 flex-col">
            <p
              className="brand text-5xl font-semibold tracking-tight md:text-6xl"
              style={{
                color: approved ? "var(--mint-700)" : "var(--result-reject)",
              }}
            >
              {result.label}
            </p>
            <p className="mt-3 text-sm leading-relaxed" style={{ color: "var(--muted)" }}>
              {approved
                ? "Applicant looks creditworthy under the selected model."
                : "Applicant did not meet the approval threshold for this model."}
            </p>

            {confidence !== null ? (
              <div className="mt-8">
                <div className="mb-2 flex items-end justify-between gap-3">
                  <span
                    className="text-sm font-medium"
                    style={{ color: "var(--muted-strong)" }}
                  >
                    Confidence
                  </span>
                  <span className="brand text-2xl font-semibold tabular-nums">
                    {(confidence * 100).toFixed(1)}%
                  </span>
                </div>
                <div
                  className="h-2.5 overflow-hidden rounded-full"
                  style={{ background: "var(--border)" }}
                >
                  <div
                    className="meter-fill h-full rounded-full"
                    style={{
                      width: `${Math.max(4, confidence * 100)}%`,
                      background: approved
                        ? "var(--mint)"
                        : "color-mix(in srgb, var(--ink) 45%, transparent)",
                    }}
                  />
                </div>
                <p className="mt-2 text-xs" style={{ color: "var(--muted-label)" }}>
                  Probability of this decision (Approved or Rejected)
                </p>
              </div>
            ) : null}

            <div
              className="mt-auto grid grid-cols-1 gap-3 border-t pt-5 sm:grid-cols-2"
              style={{ borderColor: "var(--border)" }}
            >
              <MetaCell label="Model" value={modelLabel(result.model)} />
              <MetaCell
                label="Class"
                value={result.prediction === 1 ? "1 · Approve" : "0 · Reject"}
              />
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

function MetaCell({ label, value }: { label: string; value: string }) {
  return (
    <div>
      <p
        className="text-[11px] font-medium uppercase tracking-[0.12em]"
        style={{ color: "var(--muted-label)" }}
      >
        {label}
      </p>
      <p className="mt-1 text-sm font-medium" style={{ color: "var(--ink)" }}>
        {value}
      </p>
    </div>
  );
}

function Field({
  label,
  value,
  onChange,
  type = "text",
  step,
}: {
  label: string;
  value: string;
  onChange: (v: string) => void;
  type?: string;
  step?: string;
}) {
  return (
    <label className="block">
      <span
        className="mb-2 block text-sm font-medium"
        style={{ color: "var(--muted-strong)" }}
      >
        {label}
      </span>
      <input
        className="w-full rounded-xl border px-3.5 py-2.5 text-sm outline-none ring-[var(--mint)] focus:ring-2"
        style={{
          borderColor: "var(--border-strong)",
          background: "var(--bg)",
          color: "var(--ink)",
        }}
        type={type}
        step={step}
        value={value}
        onChange={(e) => onChange(e.target.value)}
        required
      />
    </label>
  );
}

function SelectField({
  label,
  value,
  onChange,
}: {
  label: string;
  value: string;
  onChange: (v: string) => void;
}) {
  return (
    <label className="block">
      <span
        className="mb-2 block text-sm font-medium"
        style={{ color: "var(--muted-strong)" }}
      >
        {label}
      </span>
      <select
        className="w-full cursor-pointer rounded-xl border px-3.5 py-2.5 text-sm outline-none ring-[var(--mint)] focus:ring-2"
        style={{
          borderColor: "var(--border-strong)",
          background: "var(--bg)",
          color: "var(--ink)",
        }}
        value={value}
        onChange={(e) => onChange(e.target.value)}
      >
        <option value="Yes">Yes</option>
        <option value="No">No</option>
      </select>
    </label>
  );
}
