import messages from "../../messages/tr.json";

export default async function Page() {
  const res = await fetch("http://localhost:8000/valuation/AAPL");
  const data = await res.json();

  return (
    <main>
      <h1>{messages.title}</h1>
      {Object.entries(data.scenarios).map(([scenario, models]: any) => (
        <div key={scenario}>
          <h2>{messages[scenario]}</h2>
          {Object.entries(models).map(([model, value]: any) => (
            <p key={model}>{model}: ${value}</p>
          ))}
        </div>
      ))}
    </main>
  );
}
