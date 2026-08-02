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
