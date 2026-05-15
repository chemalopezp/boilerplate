import { describe, expect, it } from 'bun:test'
import app from '../src/index'

describe('health', () => {
  it('returns 200', async () => {
    const res = await app.fetch(new Request('http://localhost/api/v1/health'))
    expect(res.status).toBe(200)
    expect(await res.json()).toEqual({ status: 'ok' })
  })
})
