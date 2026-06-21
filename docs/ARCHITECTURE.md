# CareMate AI Architecture

## Overview

CareMate AI is a multi-agent family health concierge system.

## Components

### Orchestrator Agent
Routes requests to specialized agents.

### Wellness Agent
Tracks daily wellness updates.

### Medication Agent
Manages medication schedules and reminders.

### Appointment Agent
Tracks doctor appointments.

### Emergency Agent
Handles emergency contacts and escalation.

## Flow

User
  ↓
Orchestrator Agent
  ↓
 ├── Wellness Agent
 ├── Medication Agent
 ├── Appointment Agent
 └── Emergency Agent

## Tools

- Google ADK
- Gemini
- MCP Server
- Memory Store
- Notification Service
