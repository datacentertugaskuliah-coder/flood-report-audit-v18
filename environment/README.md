# Runtime provenance

No original Python/OS/package lock was included in the attachments. The assembly environment is not the experiment environment and has not been presented as one. `requirements.in` lists dependencies only and cannot guarantee exact reruns.

Run the export tool in the original notebook runtime if it still exists. It writes Python, platform, installed distribution versions and the capture time. These describe the runtime at capture; they prove neither the historical runtime nor historical training unless the authors supply that evidence. The tool exports version pins without package source URLs to avoid leaking credentials embedded in installation URLs.

Archive the executed notebook, actual run logs, package lock, and model/evidence files together. A later retraining is a new run even if the seed and configuration match. Do not overwrite original evidence with a reconstruction.
