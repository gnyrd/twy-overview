# Tweee Gpt

Knowledge base and prompts for custom OpenAI GPT. Not a running service.

## Service

No service configured.

## Cron Jobs

No cron jobs.

## Endpoints

No endpoints.

## Dependencies

No dependencies recorded.

## Environment Variables

| Variable | Defined | Referenced |
|----------|---------|------------|
| `MAILCHIMP_API_KEY` | Yes | Yes |
| `MAILCHIMP_AUDIENCE_ID` | Yes | Yes |
| `MAILCHIMP_FROM_NAME` | No | Yes |
| `MAILCHIMP_REPLY_TO` | No | Yes |
| `MAILCHIMP_SERVER` | No | Yes |

## Key Files

- `tweee-gpt/scripts/create_thumbnails.py` (entry_point)
- `tweee-gpt/scripts/download_newsletter_images.py` (entry_point)
- `tweee-gpt/scripts/extract_all_hero_images.py` (entry_point)
- `tweee-gpt/scripts/extract_all_images_bulk.py` (entry_point)
- `tweee-gpt/scripts/extract_images_from_eml.py` (entry_point)
- `tweee-gpt/scripts/remove_duplicate_images.py` (entry_point)
- `tweee-gpt/send_to_mailchimp.py` (entry_point)
- `tweee-gpt/scripts/cleanup_metadata.py` (module)
- `tweee-gpt/scripts/dedupe_all_images.py` (module)

## Lint Findings

- 🟠 **HIGH** [undefined_env_vars]: Env var MAILCHIMP_FROM_NAME is referenced but never defined in .env
- 🟠 **HIGH** [undefined_env_vars]: Env var MAILCHIMP_REPLY_TO is referenced but never defined in .env
- 🟠 **HIGH** [undefined_env_vars]: Env var MAILCHIMP_SERVER is referenced but never defined in .env
