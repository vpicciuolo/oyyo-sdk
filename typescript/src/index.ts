export type OYYOOptions = { baseUrl?: string; apiKey?: string };

export class OYYO {
  readonly baseUrl: string;
  readonly apiKey?: string;

  constructor(options: OYYOOptions = {}) {
    this.baseUrl = (options.baseUrl ?? "http://127.0.0.1:8080").replace(/\/$/, "");
    this.apiKey = options.apiKey;
  }

  private async request<T>(method: string, path: string, body?: unknown): Promise<T> {
    const headers: Record<string, string> = { Accept: "application/json" };
    if (body !== undefined) headers["Content-Type"] = "application/json";
    if (this.apiKey) headers.Authorization = `Bearer ${this.apiKey}`;
    const response = await fetch(this.baseUrl + path, { method, headers, body: body === undefined ? undefined : JSON.stringify(body) });
    if (!response.ok) throw new Error(`OYYO HTTP ${response.status}: ${await response.text()}`);
    return (await response.json()) as T;
  }

  models<T = unknown>(): Promise<T> { return this.request("GET", "/v1/models"); }
  chat<T = unknown>(payload: Record<string, unknown>): Promise<T> { return this.request("POST", "/v1/chat/completions", payload); }
  response<T = unknown>(payload: Record<string, unknown>): Promise<T> { return this.request("POST", "/v1/responses", payload); }
  memory<T = unknown>(payload: Record<string, unknown>): Promise<T> { return this.request("POST", "/oyyo/v1/memory", payload); }
  hardware<T = unknown>(): Promise<T> { return this.request("GET", "/oyyo/v1/hardware"); }
}
