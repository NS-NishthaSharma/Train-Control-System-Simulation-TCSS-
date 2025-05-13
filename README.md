# Train-Control-System-Simulation-TCSS
Communication-Based Train Control (CBTC) simulation built using Python and SimPy. This project models the operation of multiple trains on a fixed-block rail network with signaling logic and safety mechanisms. It serves as a demonstration of system modeling, simulation, and fail-safe design principles in the context of urban rail systems.

---

## Project Objectives

- Simulate a CBTC-like urban rail system with block occupancy logic.
- Implement signal control and interlocking logic to prevent collisions.
- Model train behavior under normal and degraded (blocked) conditions.
- Validate system behavior against functional safety requirements.
- Use requirement traceability techniques to ensure full coverage.

---

## 🛠️ Tech Stack

- **Language:** Python 3.10+
- **Libraries:** `SimPy`, `matplotlib` (for optional visualization)
- **Tools:** Git, VS Code/Jupyter Notebook
- **Optional:** MATLAB/Simulink (for advanced control or visualization)

---

## System Components

### 1. `Block`
Represents a section of the track that may be occupied by a train.

### 2. `Train`
A simulation agent that moves across blocks based on signal status.

### 3. `SignalController`
Determines whether a train can move to the next block or must stop.

### 4. `SimulationEngine`
Orchestrates the SimPy environment, initializes trains and track.

---

## Simulation Logic Overview

- Each block can be occupied by only one train at a time.
- Trains check the next block before moving.
- If the next block is occupied, the train waits.
- Signal status updates dynamically based on block occupancy.
- Logs are printed to monitor train positions and system state.

---

## Example Functional Requirements

| ID   | Requirement                                                             |
|------|-------------------------------------------------------------------------|
| R1   | No two trains may occupy the same block simultaneously.                |
| R2   | Trains must stop when the next block is occupied.                      |
| R3   | The system must log all train movements with timestamps.               |
| R4   | Trains must resume motion automatically once the path is clear.        |
| R5   | System must detect and prevent collisions under normal operations.     |

---

## 🧪 Test Scenarios

- **Scenario 1**: Two trains on separate tracks moving freely.
- **Scenario 2**: One train is blocked, second train halts safely.
- **Scenario 3**: Fail-safe test where simultaneous entry is attempted.

---


