import React, { useEffect, useRef } from "react";
import Plotly from "plotly.js-cartesian-dist";

const CustomPlot = (props) => {
  const plotRef = useRef(null);

  useEffect(() => {
    if (plotRef.current && props.data) {
      const plotData = props.data.map((trace) => {
        return {
          x: trace.x,
          y: trace.y,
          mode: "markers",
          type: "scatter",
          name: trace.name,
          marker: {
            color: trace.marker.color,
            size: trace.marker.size,
          },
        };
      });

      const plotLayout = {
        title: props.title,
        xaxis: { title: props.xaxisTitle },
        yaxis: { title: props.yaxisTitle },
      };

      Plotly.react(plotRef.current, plotData, plotLayout, {
        displayModeBar: false,
      });
    }
  }, [props.data, props.title, props.xaxisTitle, props.yaxisTitle]);

  useEffect(() => {
    if (plotRef.current && props.updateData) {
      Plotly.extendTraces(
        plotRef.current,
        { x: props.updateData.x, y: props.updateData.y },
        props.updateData.traceIndices,
        props.updateData.maxPoints
      );

      Plotly.restyle(
        plotRef.current,
        { "marker.color": props.updateData.markerColor },
        props.updateData.traceIndices
      );
    }
  }, [props.updateData]);

  return <div ref={plotRef} />;
};

export default CustomPlot;
