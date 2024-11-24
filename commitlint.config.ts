module.exports = {
  extends: ['@commitlint/config-conventional'],
  rules: {
    'type-enum': [2, 'always', ['feat', 'fix', 'chore', 'docs', 'style', 'refactor', 'test']],
    'subject-case': [2, 'never', ['sentence-case']],
    'scope-case': [2, 'always', 'lower-case'],
    'header-max-length': [2, 'always', 72],
  },
}
