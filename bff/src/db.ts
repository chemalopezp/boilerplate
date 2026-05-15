// Run `bunx prisma generate` after adding models to prisma/schema.prisma.
// Until then, PrismaClient types won't exist and this file will show a TS error.
import { PrismaClient } from '@prisma/client'

// Singleton — prevents multiple connections during hot reload.
const globalForPrisma = globalThis as unknown as { prisma: PrismaClient }

export const prisma =
  globalForPrisma.prisma ??
  new PrismaClient({ datasourceUrl: process.env.DATABASE_URL })

if (process.env.NODE_ENV !== 'production') globalForPrisma.prisma = prisma
