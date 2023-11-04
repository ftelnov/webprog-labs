import { useState } from "react";
import "./App.css";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import { Container, Stack } from "@mui/system";

type AppStage = "form" | "view";

/// By default interval equals 5s.
const DEFAULT_INTERVAL_MS = 5000;

type ViewSettings = {
  pages: URL[];
  interval_ms: number;
};

type InputFormProps = {
  onSettingsSubmit: (settings: ViewSettings) => void;
};

function InputForm(props: InputFormProps) {
  let [intervalInput, setIntervalInput] = useState(
    DEFAULT_INTERVAL_MS.toString(),
  );
  let [pagesInput, setPagesInput] = useState("");

  function handleIntervalInput(event: any) {
    setIntervalInput(event.target.value);
  }

  function handlePagesInput(event: any) {
    setPagesInput(event.target.value);
  }

  function handleSubmit(event: any) {
    event.preventDefault();
    let pages = pagesInput.split("\n");
    let resultWebpages = [];
    for (let page of pages) {
      // page must be pointed by a valid URL.
      try {
        let parsed = new URL(page);
        resultWebpages.push(parsed);
      } catch (TypeError) {
        toast.error(`"${page}" is not a valid URL.`);
        return;
      }
    }

    // verify interval.
    let interval = parseInt(intervalInput);
    if (isNaN(interval)) {
      toast.error(
        `Failed to parse interval: "${intervalInput}" is not a valid number`,
      );
      return;
    }
    if (interval === 0) {
      toast.error(`Interval must not be zero.`);
      return;
    }

    props.onSettingsSubmit({
      interval_ms: interval,
      pages: resultWebpages,
    });
  }

  return (
    <form onSubmit={handleSubmit}>
      <Stack spacing={2}>
        <Stack>
          <label>Webpages:</label>
          <textarea onChange={handlePagesInput} />
        </Stack>
        <Stack>
          <label>Interval(millis):</label>
          <input type="number" onChange={handleIntervalInput} />
        </Stack>
        <input type="submit" value="Начать просмотр" />
      </Stack>
    </form>
  );
}

type PagesViewProps = ViewSettings & {
  getBack: () => void;
};

function PagesGallery(props: PagesViewProps) {
  const [currentPageIdx, setCurrentPageIdx] = useState(0);

  setInterval(() => {
    let index = currentPageIdx + 1;
    if (index >= props.pages.length) {
      index = 0;
    }
    setCurrentPageIdx(index);
  }, props.interval_ms);

  return (
    <Stack spacing={2} sx={{ height: "100%" }}>
      <div className="button" onClick={props.getBack}>
        Get back
      </div>

      <iframe
        src={props.pages[currentPageIdx].toString()}
        className="page-iframe"
        title="Current Page"
      ></iframe>
    </Stack>
  );
}

function App() {
  const [stage, setStage] = useState<AppStage>("form");

  let [interval, setInterval] = useState(DEFAULT_INTERVAL_MS);
  let [pages, setPages] = useState<Array<URL>>([]);

  let currentStageComponent = null;
  if (stage === "form") {
    currentStageComponent = (
      <InputForm
        onSettingsSubmit={(settings) => {
          setPages(settings.pages);
          setInterval(settings.interval_ms);
          setStage("view");
        }}
      />
    );
  } else if (stage === "view") {
    currentStageComponent = (
      <PagesGallery
        pages={pages}
        interval_ms={interval}
        getBack={() => setStage("form")}
      />
    );
  }

  return (
    <div className="app">
      <Container className="stages-container">
        {currentStageComponent}
      </Container>
      <div className="toast-container">
        <ToastContainer />
      </div>
    </div>
  );
}

export default App;
