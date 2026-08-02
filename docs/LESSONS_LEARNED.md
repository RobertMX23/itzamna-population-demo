# Lessons Learned

## GitHub Pages and Node.js runtime

### Context

The Pages deployment completed successfully, but GitHub reported a warning
because some Pages actions still declare Node.js 20 internally while the
runner executes them on Node.js 24.

### Root cause

The warning comes from the runtime declared by the upstream actions, not from
our application code and not from an explicit `node20` setting in this demo.

### Decision

- Do not opt back into Node.js 20.
- Keep the GitHub-hosted runner on the current Node.js 24 runtime.
- Upgrade the Pages actions when the maintainers publish Node.js 24-native
  releases.
- Treat the warning as controlled technical debt while the deployment remains
  green.

### Verification

The deployment must continue to report `Success` and expose the Pages URL.
Any future action upgrade must be validated through the `deploy-pages`
workflow before merging.

### Operational rule

Warnings from an upstream action are not fixed by downgrading the runner. We
first verify whether the warning is explicit project configuration, an action
runtime, or a real execution failure.

## CI/CD DO NOT

- Do not set `ACTIONS_ALLOW_USE_UNSECURE_NODE_VERSION=true` to hide the Node
  20 warning.
- Do not downgrade the runner to Node 20.
- Do not place a GitHub PAT, INEGI token, or any secret in the repository,
  README, workflow source, or commit history.
- Do not use `enablement: true` in the Pages workflow unless the token has
  repository administration permission; enable Pages in repository settings
  or provision it with a properly scoped administrative token.
- Do not treat a green CI check as proof that Pages is configured; validate
  the deployment job and the published URL separately.
- Do not replace a working dashboard or data layer to resolve a deployment
  warning unrelated to application code.

## Design QA contract

The dashboard smoke suite treats the visual composition as a product
contract. It protects the semantic regions, the desktop grid, the mobile
breakpoint, and the no-overflow rule. A missing or altered rule fails CI and
creates a visible failed check before the change can be considered ready.
