# MCSM Roadmap

Minecraft Server Manager is developed incrementally. Each milestone should be completed, tested and committed before moving on to the next.

---

## ✅ Milestone 1 – Foundation

Completed.

- [x] Project structure
- [x] CLI
- [x] Version command
- [x] Doctor command
- [x] Status command
- [x] System services
- [x] systemd service layer
- [x] Data models
- [x] Initial test suite

---

## 🚧 Milestone 2 – Installation

In progress.

### Prerequisites

- [x] Install command
- [x] Java verification
- [x] systemd verification
- [x] Root privilege verification

### Installation

- [x] Create server directories
- [x] Download latest Paper
- [x] Create minecraft.service template

### Remaining

- [ ] Create minecraft system user
- [ ] Configure directory ownership
- [ ] Create minecraft.service
- [ ] Reload systemd daemon
- [ ] Enable minecraft.service
- [ ] Accept Minecraft EULA
- [ ] Verify installation

---

## ⏳ Milestone 3 – Server Management

- [x] Start server
- [x] Stop server
- [x] Restart server
- [ ] Enable service
- [ ] Disable service
- [ ] View server logs

---

## ⏳ Milestone 4 – Backups

- [ ] Create backup
- [ ] Restore backup
- [ ] List backups
- [ ] Automatic backups
- [ ] Backup retention policy

---

## ⏳ Milestone 5 – Updates

- [ ] Check for Paper updates
- [ ] Download update
- [ ] Install update
- [ ] Roll back update

---

## ⏳ Milestone 6 – Configuration

- [ ] Configure memory
- [ ] Configure Java flags
- [ ] Configure server.properties
- [ ] Configure MOTD
- [ ] Configure difficulty
- [ ] Configure game mode
- [ ] Configure PvP
- [ ] Configure whitelist

---

## ⏳ Milestone 7 – Player Management

### Operators

- [ ] Add operator
- [ ] Remove operator
- [ ] List operators

### Whitelist

- [ ] Add player
- [ ] Remove player
- [ ] List players

### Player Administration

- [ ] Ban player
- [ ] Unban player
- [ ] List banned players
- [ ] Kick player
- [ ] List online players
- [ ] Broadcast message
- [ ] Save world

---

## ⏳ Milestone 8 – Plugin Management

- [ ] Install plugin
- [ ] Remove plugin
- [ ] Update plugin
- [ ] Enable plugin
- [ ] Disable plugin
- [ ] List installed plugins

---

## ⏳ Milestone 9 – Monitoring

- [ ] Server resource usage
- [ ] TPS monitoring
- [ ] Memory usage
- [ ] Disk usage
- [ ] Player statistics
- [ ] Health check

---

## Future Ideas

- Interactive setup wizard
- Web dashboard
- Remote server management
- Multi-server support
- Docker backend
- Automatic scheduled updates
- Automatic restart scheduling
- RCON support
- REST API
- Discord integration